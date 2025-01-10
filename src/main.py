from textnode import TextNode
from conversions import text_node_to_html_node
    

def main():
    test_node = TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(test_node)
    print(f">>>{text_node_to_html_node(TextNode("Test", text_type="bold"))}")

main()