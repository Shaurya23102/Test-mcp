from fastmcp import FastMCP
import random 
mcp = FastMCP(name = "test")
@mcp.tool
def Dice():
    return [random.randint(1,6) for i in range(0,2)]
@mcp.tool
def add(a:int,b:int):
    return a+b
if __name__ == "__main__":
#    mcp.run()
    mcp.run(transport="http", host = "0.0.0.0" ,port = 1234)

