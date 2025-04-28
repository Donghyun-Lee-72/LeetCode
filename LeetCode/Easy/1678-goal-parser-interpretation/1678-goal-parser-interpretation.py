class Solution:
    def helper(self, command: str, result: list[str]) -> None:
        if len(command) == 0:
            return
        
        if command[0] == "G":
            result.append("G")
            self.helper(command[1:], result)
        elif command[0:2] == "()":
            result.append("o")
            self.helper(command[2:], result)
        else:
            result.append("al")
            self.helper(command[4:], result)
    
    def interpret(self, command: str) -> str:
        result = []
        self.helper(command, result)
        return "".join(result)