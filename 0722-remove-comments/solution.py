class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        result = []
        block_comment = False
        current_line = []

        for line in source:
            leng = len(line)

            i = 0
            while i < leng:
                if not block_comment and line[i:i+2] == "//":
                    break

                elif not block_comment and line[i:i+2] == "/*":
                    block_comment = True
                    i += 2
                    continue

                elif block_comment and line[i:i+2] == "*/":
                    block_comment = False
                    i += 2
                    continue

                if not block_comment:
                    current_line.append(line[i])

                i += 1

            if not block_comment:
                newLine = "".join(current_line)
                if newLine:
                    result.append(newLine)
                current_line = []

        return result
