"""Run once: python _scaffold.py  — creates all problem stub files."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

LINKED_LIST = """\

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
"""

TREE = """\

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

# (folder, category name, extra class header, [(num, slug, title, difficulty), ...])
CATEGORIES = [
    ("01_array_string", "Array / String", None, [
        ("1768", "merge-strings-alternately",                  "Merge Strings Alternately",                    "Easy"),
        ("1071", "greatest-common-divisor-of-strings",         "Greatest Common Divisor of Strings",           "Easy"),
        ("1431", "kids-with-the-greatest-number-of-candies",   "Kids With the Greatest Number of Candies",     "Easy"),
        ("605",  "can-place-flowers",                          "Can Place Flowers",                            "Easy"),
        ("345",  "reverse-vowels-of-a-string",                 "Reverse Vowels of a String",                   "Easy"),
        ("443",  "string-compression",                         "String Compression",                           "Medium"),
        ("238",  "product-of-array-except-self",               "Product of Array Except Self",                 "Medium"),
        ("334",  "increasing-triplet-subsequence",             "Increasing Triplet Subsequence",               "Medium"),
    ]),
    ("02_two_pointers", "Two Pointers", None, [
        ("283",  "move-zeroes",                                "Move Zeroes",                                  "Easy"),
        ("392",  "is-subsequence",                             "Is Subsequence",                               "Easy"),
        ("11",   "container-with-most-water",                  "Container With Most Water",                    "Medium"),
        ("1679", "max-number-of-k-sum-pairs",                  "Max Number of K-Sum Pairs",                    "Medium"),
    ]),
    ("03_sliding_window", "Sliding Window", None, [
        ("643",  "maximum-average-subarray-i",                 "Maximum Average Subarray I",                   "Easy"),
        ("1456", "maximum-number-of-vowels-in-a-substring-of-given-length",
                                                               "Maximum Number of Vowels in a Substring of Given Length", "Medium"),
        ("1004", "max-consecutive-ones-iii",                   "Max Consecutive Ones III",                     "Medium"),
        ("1493", "longest-subarray-of-1s-after-deleting-one-element",
                                                               "Longest Subarray of 1's After Deleting One Element", "Medium"),
    ]),
    ("04_prefix_sum", "Prefix Sum", None, [
        ("1732", "find-the-highest-altitude",                  "Find the Highest Altitude",                    "Easy"),
        ("724",  "find-pivot-index",                           "Find Pivot Index",                             "Easy"),
    ]),
    ("05_hash_map_set", "Hash Map / Set", None, [
        ("2215", "find-the-difference-of-two-arrays",          "Find the Difference of Two Arrays",            "Easy"),
        ("1207", "unique-number-of-occurrences",               "Unique Number of Occurrences",                 "Easy"),
        ("1657", "determine-if-two-strings-are-close",         "Determine if Two Strings Are Close",           "Medium"),
        ("2352", "equal-row-and-column-pairs",                 "Equal Row and Column Pairs",                   "Medium"),
    ]),
    ("06_stack", "Stack", None, [
        ("2390", "removing-stars-from-a-string",               "Removing Stars From a String",                 "Medium"),
        ("735",  "asteroid-collision",                         "Asteroid Collision",                           "Medium"),
        ("394",  "decode-string",                              "Decode String",                                "Medium"),
    ]),
    ("07_queue", "Queue", None, [
        ("933",  "number-of-recent-calls",                     "Number of Recent Calls",                       "Easy"),
        ("649",  "dota2-senate",                               "Dota2 Senate",                                 "Medium"),
    ]),
    ("08_linked_list", "Linked List", LINKED_LIST, [
        ("2095", "delete-the-middle-node-of-a-linked-list",    "Delete the Middle Node of a Linked List",      "Medium"),
        ("328",  "odd-even-linked-list",                       "Odd Even Linked List",                         "Medium"),
        ("206",  "reverse-linked-list",                        "Reverse Linked List",                          "Easy"),
        ("2130", "maximum-twin-sum-of-a-linked-list",          "Maximum Twin Sum of a Linked List",            "Medium"),
    ]),
    ("09_binary_tree_dfs", "Binary Tree — DFS", TREE, [
        ("104",  "maximum-depth-of-binary-tree",               "Maximum Depth of Binary Tree",                 "Easy"),
        ("872",  "leaf-similar-trees",                         "Leaf-Similar Trees",                           "Easy"),
        ("1448", "count-good-nodes-in-binary-tree",            "Count Good Nodes in Binary Tree",              "Medium"),
        ("437",  "path-sum-iii",                               "Path Sum III",                                 "Medium"),
        ("1372", "longest-zigzag-path-in-a-binary-tree",       "Longest ZigZag Path in a Binary Tree",         "Medium"),
    ]),
    ("10_binary_tree_bfs", "Binary Tree — BFS", TREE, [
        ("199",  "binary-tree-right-side-view",                "Binary Tree Right Side View",                  "Medium"),
        ("1161", "maximum-level-sum-of-a-binary-tree",         "Maximum Level Sum of a Binary Tree",           "Medium"),
        ("637",  "average-of-levels-in-binary-tree",           "Average of Levels in Binary Tree",             "Easy"),
    ]),
    ("11_binary_search_tree", "Binary Search Tree", TREE, [
        ("700",  "search-in-a-binary-search-tree",             "Search in a Binary Search Tree",               "Easy"),
        ("450",  "delete-node-in-a-bst",                       "Delete Node in a BST",                        "Medium"),
    ]),
    ("12_graphs_dfs", "Graphs — DFS", None, [
        ("841",  "keys-and-rooms",                             "Keys and Rooms",                               "Medium"),
        ("547",  "number-of-provinces",                        "Number of Provinces",                          "Medium"),
        ("1466", "reorder-routes-to-make-all-paths-lead-to-the-city-zero",
                                                               "Reorder Routes to Make All Paths Lead to the City Zero", "Medium"),
    ]),
    ("13_graphs_bfs", "Graphs — BFS", None, [
        ("1926", "nearest-exit-from-entrance-in-maze",         "Nearest Exit from Entrance in Maze",           "Medium"),
        ("994",  "rotting-oranges",                            "Rotting Oranges",                              "Medium"),
    ]),
    ("14_heap_priority_queue", "Heap / Priority Queue", None, [
        ("2336", "smallest-number-in-infinite-set",            "Smallest Number in Infinite Set",              "Medium"),
        ("2542", "maximum-subsequence-score",                  "Maximum Subsequence Score",                    "Medium"),
        ("2462", "total-cost-to-hire-k-workers",               "Total Cost to Hire K Workers",                 "Medium"),
    ]),
    ("15_binary_search", "Binary Search", None, [
        ("374",  "guess-number-higher-or-lower",               "Guess Number Higher or Lower",                 "Easy"),
        ("2300", "successful-pairs-of-spells-and-potions",     "Successful Pairs of Spells and Potions",       "Medium"),
        ("162",  "find-peak-element",                          "Find Peak Element",                            "Medium"),
        ("875",  "koko-eating-bananas",                        "Koko Eating Bananas",                          "Medium"),
    ]),
    ("16_backtracking", "Backtracking", None, [
        ("17",   "letter-combinations-of-a-phone-number",      "Letter Combinations of a Phone Number",        "Medium"),
        ("216",  "combination-sum-iii",                        "Combination Sum III",                          "Medium"),
    ]),
    ("17_dp_1d", "Dynamic Programming — 1D", None, [
        ("1137", "n-th-tribonacci-number",                     "N-th Tribonacci Number",                       "Easy"),
        ("746",  "min-cost-climbing-stairs",                   "Min Cost Climbing Stairs",                     "Easy"),
        ("198",  "house-robber",                               "House Robber",                                 "Medium"),
        ("790",  "domino-and-tromino-tiling",                  "Domino and Tromino Tiling",                    "Medium"),
    ]),
    ("18_dp_multidim", "Dynamic Programming — Multidimensional", None, [
        ("62",   "unique-paths",                               "Unique Paths",                                 "Medium"),
        ("1143", "longest-common-subsequence",                 "Longest Common Subsequence",                   "Medium"),
        ("714",  "best-time-to-buy-and-sell-stock-with-transaction-fee",
                                                               "Best Time to Buy and Sell Stock with Transaction Fee", "Medium"),
        ("72",   "edit-distance",                              "Edit Distance",                                "Medium"),
        ("309",  "best-time-to-buy-and-sell-stock-with-cooldown",
                                                               "Best Time to Buy and Sell Stock with Cooldown", "Medium"),
    ]),
    ("19_bit_manipulation", "Bit Manipulation", None, [
        ("338",  "counting-bits",                              "Counting Bits",                                "Easy"),
        ("136",  "single-number",                              "Single Number",                                "Easy"),
        ("1318", "minimum-flips-to-make-a-or-b-equal-to-c",   "Minimum Flips to Make a OR b Equal to c",      "Medium"),
    ]),
    ("20_trie", "Trie", None, [
        ("208",  "implement-trie-prefix-tree",                 "Implement Trie (Prefix Tree)",                 "Medium"),
        ("1268", "search-suggestions-system",                  "Search Suggestions System",                    "Medium"),
    ]),
    ("21_intervals", "Intervals", None, [
        ("57",   "insert-interval",                            "Insert Interval",                              "Medium"),
        ("435",  "non-overlapping-intervals",                  "Non-overlapping Intervals",                    "Medium"),
        ("452",  "minimum-number-of-arrows-to-burst-balloons", "Minimum Number of Arrows to Burst Balloons",   "Medium"),
    ]),
    ("22_monotonic_stack", "Monotonic Stack", None, [
        ("739",  "daily-temperatures",                         "Daily Temperatures",                           "Medium"),
        ("901",  "online-stock-span",                          "Online Stock Span",                            "Medium"),
        ("496",  "next-greater-element-i",                     "Next Greater Element I",                       "Easy"),
    ]),
]


def slug_to_camel(slug: str) -> str:
    words = slug.split("-")
    return words[0] + "".join(w.capitalize() for w in words[1:])


def make_file(folder: str, num: str, slug: str, title: str, diff: str, extra: str | None):
    method = slug_to_camel(slug)
    filename = f"{num}_{slug.replace('-', '_')}.py"
    filepath = os.path.join(BASE, folder, filename)

    if os.path.exists(filepath):
        return  # never overwrite existing solutions

    imports = "from typing import List, Optional\n"
    class_block = extra if extra else ""

    content = (
        f"# {num}. {title}\n"
        f"# Difficulty: {diff}\n"
        f"# https://leetcode.com/problems/{slug}/\n"
        f"\n"
        f"{imports}"
        f"{class_block}"
        f"\n"
        f"class Solution:\n"
        f"    def {method}(self):\n"
        f"        pass\n"
        f"\n"
        f"\n"
        f'if __name__ == "__main__":\n'
        f"    sol = Solution()\n"
        f"    # Add your test cases here\n"
    )

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)


total = 0
for folder, cat_name, extra_header, problems in CATEGORIES:
    dir_path = os.path.join(BASE, folder)
    os.makedirs(dir_path, exist_ok=True)
    for num, slug, title, diff in problems:
        make_file(folder, num, slug, title, diff, extra_header)
        total += 1

print(f"Created stubs for {total} problems across {len(CATEGORIES)} categories.")
