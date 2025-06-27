class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_counts = defaultdict(int)

        for current_row in grid: 
            row_tuple = tuple(current_row)
            row_counts[row_tuple] += 1
        
        total_equal_pairs = 0
        for current_column in zip(*grid):
            print(current_column)
            column_tuple = tuple(current_column)
            total_equal_pairs += row_counts[column_tuple]

        return total_equal_pairs
