from openai import OpenAI
import re
from pypinyin import pinyin, Style


def call_llm(api_key: str, prompt: str, sys_prompt: str) -> dict:
    client = OpenAI(
        api_key=api_key,
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )
    completion = client.chat.completions.create(
        model="qwen-plus",
        messages=[
            {
                "role": "system",
                "content": sys_prompt,
            },
            {"role": "user", "content": prompt},
        ],
        temperature=0.8,
    )
    response = completion.choices[0].message.content
    return response


prompt_dict = {
    "subject_prompt": {
        "sys_prompt": "Only one English word or phrase is returned",
        "prompt": "Use the above text to sort the person's description by topic and return just one English word or phrase:",
    },
    "contribution_prompt": {
        "sys_prompt": "你是评审人员，擅长评审他人的工作",
        "prompt": " 结合以上人物介绍，不要出现人名，不要主语，最后不要句号。用夸张且诙谐的一句中文不超过20个词不带主语的话总结他的主要贡献，可以非常主观: ",
    },
}

prompt_dict_en = {
    "subject_prompt": {
        "sys_prompt": "Only one English word or phrase is returned",
        "prompt": "Use the above text to sort the person's description by topic and return just one English word or phrase:",
    },
    "contribution_prompt": {
        "sys_prompt": "You're a reviewer, and you're good at reviewing other people's work. Only return English",
        "prompt": "Combined with the above character introduction, summarize his main contributions in a one-sentence short play without subject or punctuation. Exaggerate to emphasize the great contribution. Only return English And no more than 20 words: ",
    },
}


def is_chinese(char):
    """判断一个字符是否为中文"""
    return "\u4e00" <= char <= "\u9fff"


def standardize_name(name):
    """将输入的名字转化为学术英语的标准格式"""
    if any(is_chinese(char) for char in name):
        # 使用pypinyin库将中文名转为拼音
        parts = pinyin(name, style=Style.NORMAL)

        parts = [part[0] for part in parts]  # 不进行大写转换，直接连成字符串
        # 假设最后一个部分是姓，其他是名
        first_name = "".join(parts[1:]).capitalize()  # 连接并首字母大写
        last_name = parts[0].capitalize()  # 姓的首字母大写
        # 转换为首字母大写的格式，并调整顺序
        return f"{first_name} {last_name}"
    else:
        # 如果名字不含中文，直接返回
        return name


def get_slogan(content, name, prompt_dict, api_key):

    name = standardize_name(name)

    subject_prompt = prompt_dict["subject_prompt"]
    sys_prompt = subject_prompt["sys_prompt"]
    prompt = content + subject_prompt["prompt"]
    subject = call_llm(api_key, prompt, sys_prompt)
    subject_content = f"THE NOBEL PRIZE IN {subject.upper()} 2024"

    contribution_prompt = prompt_dict["contribution_prompt"]
    sys_prompt = contribution_prompt["sys_prompt"]
    prompt = content + contribution_prompt["prompt"] + content
    contribution_content = "”" + call_llm(api_key, prompt, sys_prompt).strip() + "“"

    return subject_content, name, contribution_content


if __name__ == "__main__":
    api_key = ""
    name = "somebody"
    content = "Do nothing"
    prompt_dict = prompt_dict
    subject_content, name, contribution_content = get_slogan(
        content, name, prompt_dict, api_key
    )
    print(subject_content)
    print(name)
    print(contribution_content)
