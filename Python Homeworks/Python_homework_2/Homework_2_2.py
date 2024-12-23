class DataBuffer:
    def __init__(self):
        self.buffer = [] # Инициализируем буфер

    def add_data(self, data):
        self.buffer.append(data)
        if len(self.buffer) >= 5:
            self.buffer.clear()
            print("Буффер переполнен. Очищено.")

    def get_data(self):
        if not self.buffer:
            print("В буфере нет данных.")
            return None
        else:
            return self.buffer
