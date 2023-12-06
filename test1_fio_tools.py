from subprocess import Popen, PIPE
from fio_tools import Fiomethods
import time
import threading

working_directory = '/home/ubuntu/hemanth'

class TestSequentialOperations:

    def run_fio_test(self, test_name, operation, size, num_jobs, num_seconds, **kwargs):
        read_test = Fiomethods()
        command = read_test.run_test(test_name, operation, size, num_jobs, num_seconds, **kwargs)

        process = Popen(command, stdout=PIPE, stderr=PIPE, text=True, cwd=working_directory)
        stdout, stderr = process.communicate()
        assert process.returncode == 0, f"Test failed. Command output:\n{stdout}\n{stderr}"

    def test_sequential_read(self):
        self.run_fio_test('seqread', 'read', '1G', 1, 20)
    def test_sequential_write(self):
         self.run_fio_test('seqwrite', 'write', '1G', 1, 20)
    def test_random_read(self):
         self.run_fio_test('randwrite', 'randwrite', '1G', 1, 20)
    def test_random_write(self):
         self.run_fio_test('randwrite', 'randwrite', '1G', 1, 20)
    def test_mixed_read_write(self):
         self.run_fio_test('randrw', 'randrw', '1G', 1, 30, rwmixread=70)
    def test_sequential_read_mul(self):
         self.run_fio_test('seqread_multi', 'read', '1G', 4, 20)
    def test_random_read_mul(self):
         self.run_fio_test('randread_multi', 'read', '1G', 4, 20)
    def test_iops_Latency(self):
         self.run_fio_test('iops_latency', 'randwrite', '1G', 1, 20, output_format='json', output='iops_latency_results.json')
    def test_throughput(self):
         self.run_fio_test('throughput_test', 'randwrite', '1G', 1, 20, output_format='json', output='throughput_results.json')
    def test_run_tests_in_parallel(self):
        thread1 = threading.Thread(target=self.test_sequential_read)
        thread2 = threading.Thread(target=self.test_random_write)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

if __name__ == "__main__":
    test_instance = TestSequentialOperations()
    test_instance.test_run_tests_in_parallel()
