import yaml
import sys

file = str(sys.argv[1])
release = str(sys.argv[2])
env = str(sys.argv[3])

def read_file(file):
    with open(file) as stream:
        return yaml.safe_load(stream)

def apply_changes(yamlfile, release, env):
    yamlfile['spec']['data']['image']['tag'] = release
    yamlfile['spec']['data']['configmap']['data'] = f'ENV: {env}'
    return yamlfile

def write_file(file, yamlfile):
    with open(file, "w") as f:
        yaml.dump(yamlfile, f)

yamlfile = read_file(file)
apply_changes(yamlfile, release, env)
write_file(file, yamlfile)