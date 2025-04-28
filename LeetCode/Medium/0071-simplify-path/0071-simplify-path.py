class Solution:
    def simplifyPath(self, path: str) -> str:
        path_filtered = filter(None, path.split("/"))
        path_list = list(path_filtered)
        idx = 0
        while idx < len(path_list):
            directory = path_list[idx]
            if directory == ".":
                path_list.pop(idx)
            elif directory == "..":
                if idx == 0:
                    path_list.pop(idx)
                else:
                    path_list.pop(idx)
                    path_list.pop(idx-1)
                    idx -= 1
            else:
                idx += 1
                
        canonical = "/" + "/".join(path_list)
        return canonical
        