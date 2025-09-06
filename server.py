from fastmcp import FastMCP
import pathlib
import pandas as pd

# Tạo MCP server với tên mặc định
mcp = FastMCP(name="MyFastMCPServer")

# Đường dẫn tới file template testcase
STYLE_FILE_PATH = pathlib.Path("D:\\AI\\MCP-server\\testcase.txt")
STYLE_FILE = STYLE_FILE_PATH.read_text(encoding="utf-8")

# Tool 1: sinh test case theo template
@mcp.tool()
def generate_testcases(requirement: str, num_cases: int = 2) -> str:
    """
    Sinh test case theo requirement dựa trên template style
    """
    return f"{STYLE_FILE}\n\nYêu cầu: {requirement}\nSố lượng: {num_cases}\n\nViết test case theo đúng format trên."

# Tool 2: đọc file txt và xuất thành bảng Markdown
@mcp.tool()
def read_txt_as_table(file_path: str = str(STYLE_FILE_PATH)) -> str:
    """
    Đọc file .txt (định dạng CSV-like hoặc tab-delimited) và trả về bảng dưới dạng Markdown.
    Mặc định đọc testcase.txt
    """
    try:
        # Thử đọc file theo dạng CSV với phân tách dấu phẩy
        try:
            df = pd.read_csv(file_path)
        except Exception:
            # Nếu không được thì thử phân tách theo tab hoặc nhiều khoảng trắng
            df = pd.read_csv(file_path, sep=r"\s+", engine="python")
        return df.to_markdown(index=False)
    except Exception as e:
        return f" Error khi đọc file: {str(e)}"

if __name__ == "__main__":
    print("MCP Server started...")
    mcp.run()

