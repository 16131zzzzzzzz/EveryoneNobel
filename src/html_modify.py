from bs4 import BeautifulSoup


class HtmlModifier:
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_html()

    def load_html(self):
        """加载HTML文件并解析"""
        with open(self.file_path, "r", encoding="utf-8") as file:
            self.html_content = file.read()
        self.soup = BeautifulSoup(self.html_content, "html.parser")

    def update_subject(self, new_text):
        """更新主题文本"""
        subject = self.soup.find(class_="subject")
        if subject:
            subject.string = new_text

    def update_name(self, new_text):
        """更新名字文本"""
        name = self.soup.find(class_="name")
        if name:
            name.string = new_text

    def update_contribution(self, new_text):
        """更新贡献文本"""
        contribution = self.soup.find(class_="contribution")
        if contribution:
            contribution.string = new_text

    def update_footer(self, new_text):
        """更新底部文本"""
        footer = self.soup.find(class_="footer")
        if footer:
            footer.string = new_text

    def update_image_source(self, new_src):
        """更新图片源"""
        img = self.soup.find("img", id="img1")
        if img:
            img["src"] = new_src

    def update_style(self, class_name, property_name, value):
        """更新指定类的CSS样式"""
        element = self.soup.find(class_=class_name)
        if element and "style" in element.attrs:
            # 修改现有的style属性
            styles = element["style"].split(";")
            new_styles = []
            for style in styles:
                if style.strip() and property_name in style:
                    # 修改指定的样式属性
                    new_styles.append(f"{property_name}: {value}")
                else:
                    new_styles.append(style)
            element["style"] = "; ".join(new_styles) + ";"  # 更新style属性
        elif element:
            # 如果没有style属性，则创建一个
            element["style"] = f"{property_name}: {value};"

    def save_changes(self, new_path):
        """保存修改后的HTML内容"""
        with open(new_path, "w", encoding="utf-8") as file:
            file.write(str(self.soup))


class HtmlModifierDouble(HtmlModifier):
    def __init__(self, file_path):
        self.file_path = file_path
        self.load_html()

    def update_image_source2(self, new_src):
        """更新图片源"""
        img = self.soup.find("img", id="img2")
        if img:
            img["src"] = new_src

    def update_name2(self, new_text):
        """更新名字文本"""
        name = self.soup.find(class_="name1")
        if name:
            name.string = new_text


def modifier_html_double(
    html_template_path,
    subject_content,
    name,
    name2,
    contribution_content,
    img_path,
    img_path2,
):
    # 使用示例
    html_modifier = HtmlModifierDouble(html_template_path)

    subject_content_sencond_row = subject_content.split("<br>")[-1]
    subject_content_font = int(30 * min(60 / len(subject_content), 1))

    contribution_content_font = int(20 * min(1, 120 / len(contribution_content)))
    # 修改内容
    html_modifier.update_subject(subject_content)
    html_modifier.update_name(name)
    html_modifier.update_contribution(contribution_content)

    html_modifier.update_image_source(img_path)
    html_modifier.update_image_source2(img_path2)
    html_modifier.update_name2(name2)
    html_modifier.update_style(
        "subject", "font-size", f"{subject_content_font}px"
    )  # 更新名字字体大小
    html_modifier.update_style(
        "contribution", "font-size", f"{contribution_content_font}px"
    )  # 更新名字字体大小
    return html_modifier


def modifier_html(
    html_template_path, subject_content, name, contribution_content, img_path
):
    # 使用示例
    html_modifier = HtmlModifier(html_template_path)

    subject_content_sencond_row = subject_content.split("<br>")[-1]
    subject_content_font = int(30 * min(60 / len(subject_content), 1))

    contribution_content_font = int(20 * min(1, 120 / len(contribution_content)))
    # 修改内容
    html_modifier.update_subject(subject_content)
    html_modifier.update_name(name)
    html_modifier.update_contribution(contribution_content)

    html_modifier.update_image_source(img_path)
    html_modifier.update_style(
        "subject", "font-size", f"{subject_content_font}px"
    )  # 更新名字字体大小
    html_modifier.update_style(
        "contribution", "font-size", f"{contribution_content_font}px"
    )  # 更新名字字体大小
    return html_modifier


if __name__ == "__main__":
    html_template_path = "canvas.html"
    new_path = "1.html"
    subject_content = "THE NOBEL PRIZE IN COMPUTER SCIENCE 2024"
    name = "Zhihong Zhu"
    contribution_content = "”玩原神玩的“"
    img_path = "zhu.png"
    img_path2 = "zhu.png"
    name2 = "原神"
    html_modifier = modifier_html(
        html_template_path, subject_content, name, contribution_content, img_path
    )
    # html_modifier = modifier_html_double(html_template_path,subject_content,name,name2,contribution_content,img_path,img_path2)
    html_modifier.save_changes(new_path)
