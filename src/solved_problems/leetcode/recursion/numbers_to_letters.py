"""
Convert a non-negative integer num to its English words representation.

"""

class Solution:

    below_ten = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    below_twenty = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    below_hundred = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"
        # Call the helper function to start the conversion
        return self._convert_to_words(num)
    
    def _convert_to_words(self, num: int) -> str:
        if num < 10:
            return self.below_ten[num]
        if num < 20:
            return self.below_twenty[num - 10]
        if num < 100:
            return self.below_hundred[num // 10] + (" " + self._convert_to_words(num % 10) if num % 10 != 0 else "")
        if num < 1000:
            return self._convert_to_words(num // 100) + " Hundred" + (" " + self._convert_to_words(num % 100) if num % 100 != 0 else "")
        if num < 1000000:
            return self._convert_to_words(num // 1000) + " Thousand" + (" " + self._convert_to_words(num % 1000) if num % 1000 != 0 else "")
        if num < 1000000000:
            return self._convert_to_words(num // 1000000) + " Million" + (" " + self._convert_to_words(num % 1000000) if num % 1000000 != 0 else "")
        return self._convert_to_words(num // 1000000000) + " Billion" + (" " + self._convert_to_words(num % 1000000000) if num % 1000000000 != 0 else "")
    

if __name__ == "__main__":
    print(f'Welcome to numbers to letters ......')
    SOL = Solution()
    num = 123
    print(SOL.numberToWords(num))
    num = 12345
    print(SOL.numberToWords(num))
    num = 1234567
    print(SOL.numberToWords(num))







