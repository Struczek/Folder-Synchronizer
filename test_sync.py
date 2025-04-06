import unittest
import os
import tempfile
import shutil
from controllers.sync_controller import sync_folders 

class TestSyncFolders(unittest.TestCase):

    def setUp(self):
        self.source = tempfile.mkdtemp()
        self.replica = tempfile.mkdtemp()

    def tearDown(self):
        shutil.rmtree(self.source)
        shutil.rmtree(self.replica)

    def test_sync_new_file(self):
        file_path = os.path.join(self.source, "test.txt")
        with open(file_path, "w") as f:
            f.write("Hello, world!")

        sync_folders(self.source, self.replica)

        self.assertTrue(os.path.exists(os.path.join(self.replica, "test.txt")))

    def test_sync_updated_file(self):
        src_file = os.path.join(self.source, "test.txt")
        with open(src_file, "w") as f:
            f.write("Hello, world!")

        dst_file = os.path.join(self.replica, "test.txt")
        with open(dst_file, "w") as f:
            f.write("Old content")

        sync_folders(self.source, self.replica)

        with open(dst_file, "r") as f:
            content = f.read()
        self.assertEqual(content, "Hello, world!")

    def test_deleted_file_in_replica(self):
        src_file = os.path.join(self.source, "test.txt")
        with open(src_file, "w") as f:
            f.write("Hello!")

        dst_file = os.path.join(self.replica, "test.txt")
        with open(dst_file, "w") as f:
            f.write("Old content")

        sync_folders(self.source, self.replica)
        os.remove(src_file)  # delete from source

        sync_folders(self.source, self.replica)
        self.assertFalse(os.path.exists(dst_file))

if __name__ == "__main__":
    unittest.main()
