def forZipped(func):
    def wrapper(self, message: str, key: str) -> str:
        zipped = zip(message, key)
        result_list = []

        for (m, k) in zipped:
            result_list.append(func(self, m, k))

        return ''.join(result_list)
    return wrapper