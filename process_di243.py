
import re
import sys

def process_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 保存代码块、行内代码、链接、图片
    code_blocks = []
    inline_codes = []
    links = []
    images = []
    
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f'__CODE_BLOCK_{len(code_blocks)-1}__'
    
    def save_inline_code(match):
        inline_codes.append(match.group(0))
        return f'__INLINE_CODE_{len(inline_codes)-1}__'
    
    def save_link(match):
        links.append(match.group(0))
        return f'__LINK_{len(links)-1}__'
    
    def save_image(match):
        images.append(match.group(0))
        return f'__IMAGE_{len(images)-1}__'
    
    # 保存代码块
    content = re.sub(r'```.*?```', save_code_block, content, flags=re.DOTALL)
    
    # 保存行内代码
    content = re.sub(r'`[^`]+`', save_inline_code, content)
    
    # 保存图片
    content = re.sub(r'!\[.*?\]\(.*?\)', save_image, content)
    
    # 保存链接
    content = re.sub(r'\[.*?\]\(.*?\)', save_link, content)
    
    # 处理中英文之间的空格
    # 中文与英文/数字之间加空格
    content = re.sub(r'([\u4e00-\u9fa5])([a-zA-Z0-9])', r'\1 \2', content)
    content = re.sub(r'([a-zA-Z0-9])([\u4e00-\u9fa5])', r'\1 \2', content)
    
    # 中文与括号等特殊字符之间加空格
    content = re.sub(r'([\u4e00-\u9fa5])([\(\[\{])', r'\1 \2', content)
    content = re.sub(r'([\)\]\}])([\u4e00-\u9fa5])', r'\1 \2', content)
    
    # 修复一些常见的错误
    content = re.sub(r'([\u4e00-\u9fa5]),\s*([\u4e00-\u9fa5])', r'\1，\2', content)
    content = re.sub(r'([\u4e00-\u9fa5])\.\s*([\u4e00-\u9fa5])', r'\1。\2', content)
    content = re.sub(r'([\u4e00-\u9fa5])!\s*([\u4e00-\u9fa5])', r'\1！\2', content)
    content = re.sub(r'([\u4e00-\u9fa5])\?\s*([\u4e00-\u9fa5])', r'\1？\2', content)
    content = re.sub(r'([\u4e00-\u9fa5]);\s*([\u4e00-\u9fa5])', r'\1；\2', content)
    content = re.sub(r'([\u4e00-\u9fa5]):\s*([\u4e00-\u9fa5])', r'\1：\2', content)
    
    # 替换英文引号为中文引号
    content = re.sub(r'"([^"]+)"', r'“\1”', content)
    
    # 替换英文括号为中文括号（但要小心，因为括号在技术内容中很常见）
    # 这里我们只替换纯中文文本中的括号
    def replace_parentheses(match):
        text = match.group(1)
        if any('\u4e00-\u9fa5' in c for c in text):
            return f'（{text}）'
        return match.group(0)
    
    # 先不自动替换括号，因为技术文档中很多英文括号是必要的
    
    # 恢复链接
    for i, link in enumerate(links):
        content = content.replace(f'__LINK_{i}__', link)
    
    # 恢复图片
    for i, image in enumerate(images):
        content = content.replace(f'__IMAGE_{i}__', image)
    
    # 恢复行内代码
    for i, code in enumerate(inline_codes):
        content = content.replace(f'__INLINE_CODE_{i}__', code)
    
    # 恢复代码块
    for i, block in enumerate(code_blocks):
        content = content.replace(f'__CODE_BLOCK_{i}__', block)
    
    return content

if __name__ == '__main__':
    file_path = r'c:\Users\ykla\Documents\FreeBSD-Ask\di-24-zhang-kernel\di-24.3-kernel-mi.md'
    processed = process_markdown(file_path)
    
    output_path = r'c:\Users\ykla\Documents\FreeBSD-Ask\di-24-zhang-kernel\di-24.3-kernel-mi_processed.md'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(processed)
    
    print(f'处理完成，输出文件：{output_path}')
