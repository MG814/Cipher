from buffer import Text, Buffer


class TestBuffer:
    def setup_method(self):
        self.buffer = Buffer()
        self.text = Text("ddsf", "encrypted", "rot13")

    def test_buffer_add_data_method(self):
        assert len(self.buffer.data) == 0
        self.buffer.add_data(self.text)
        assert len(self.buffer.data) == 1

    def test_buffer_clear_buffer_method(self):
        self.buffer.add_data(self.text)
        assert len(self.buffer.data) != 0
        self.buffer.clear_buffer()
        assert len(self.buffer.data) == 0
