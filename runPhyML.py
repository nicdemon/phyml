import os

from subprocess import Popen, PIPE

class PhyML():
    def __init__(self, config):
        # Dynamic content
        self.cmd = []
        self.config = config
        # Static content
        self._exec = os.path.join('binaries','PhyML-3.1_linux64')
        # Execution
        self._generate_cmd()

    def run(self):
        proc = Popen(self.cmd, shell = True, stdout = PIPE)
        while proc.poll() is None:
            yield proc.poll()
        return proc.poll()
    
    def get_results(self):
        input = self.config['input']
        files = {
            "input": input,
            "tree": f"{input}_phyml_tree.txt",
            "stats": f"{input}_phyml_stats.txt",
            "trace": f"{input}_phyml_trace.txt",
            "site_lnl": f"{input}_phyml_lk.txt",
        }
        files = self._read_results(files)
        return files

    def _generate_cmd(self):
        self.cmd = [
            self._exec,
            f"-i {self.config['input']}",
            f"-d {self.config['datatype']}",
            f"-n {self.config['multiple']}",
            f"-b {self.config['bootstrap']}",
            f"-m {self.config['model']}",
            f"-f {self.config['equilibrium']}",
            f"-t {self.config['ts/tv']}",
            f"-v {self.config['pinv']}",
            f"-c {self.config['nclasses']}",
            f"-a {self.config['alpha']}",
            f"-s {self.config['search']}",
            f"-u {self.config['params']}",
        ]
        if self.config['sequential']:
            self.cmd.append("-q")
        
        if self.config['pars']:
            self.cmd.append("-p")

        if self.config['search'] == "SPR":
            self.cmd.append(f"--rand_start {self.config['rand_start']}")
            self.cmd.append(f"--n_rand_starts {self.config['n_rand_starts']}")
        
        self.cmd.append("--quiet")
        self.cmd.append("--print_trace")
        self.cmd.append("--print_site_lnl")
    
    def _read_results(self, files):
        print(files)
        for key, file in files.items():
            with open(file) as handle:
                files[key] = handle.readlines()
        return files