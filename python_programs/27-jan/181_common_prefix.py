def longest_common_prefix(strings):
    """
    Find the longest common prefix among a list of strings.

    Args:
        strings (list of str): A list of input strings.

    Returns:
        str: The longest common prefix shared by all strings.
             Returns an empty string if there is no common prefix
             or if the input list is empty.
    """
    if not strings:
        return ""

    prefix = strings[0]

    for s in strings[1:]:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    return prefix


words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))
