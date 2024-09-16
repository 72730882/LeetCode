class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        if divisor == 0:
            return 0
        is_negative = (dividend < 0) != (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0
        while dividend >= divisor:
            temp_divisor, count =divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                count <<= 1
            dividend -= temp_divisor
            quotient += count
        return -quotient if is_negative else quotient

            