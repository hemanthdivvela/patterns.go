class Fiomethods:
    def run_test(self, test_name, rw, size, numjobs, runtime, rwmixread=None, output=None, output_format=None):
        command = [
            'fio',
            '--name=' + test_name,
            '--ioengine=sync',
            '--rw=' + rw,
            '--bs=4k',
            '--size=' + size,
            '--numjobs=' + str(numjobs),
            '--time_based',
            '--runtime=' + str(runtime)
        ]
        if rwmixread is not None:
            command.append('--rwmixread=' + str(rwmixread))

        if output_format is not None:
            command.append('--output-format=' + str(output_format))
        if output is not None:
            command.append('--output=' + str(output))
        return command
