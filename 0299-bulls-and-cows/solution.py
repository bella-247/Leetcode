class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        # { num : [secret_count, bulls, cows] }
        counts = defaultdict(lambda: [0, 0, 0])

        for i in range(len(secret)):
            secret_num, guess_num = secret[i], guess[i]
            if secret_num == guess_num:
                # update the bull count
                counts[guess_num][1] += 1
            else:
                # update the cows count
                counts[guess_num][2] += 1

            counts[secret_num][0] += 1

        total_bulls = 0
        total_cows = 0

        for num in counts:
            secret_count, bulls, cows = counts[num]
            total_bulls += bulls 
            total_cows += min(secret_count - bulls, cows) # the minimum of the unused secret counts and cows

        return f"{total_bulls}A{total_cows}B"