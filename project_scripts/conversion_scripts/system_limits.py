import resource
soft, hard = resource.getrlimit(resource.RLIMIT_CPU)
print(soft, hard)
soft, hard = resource.getrlimit(resource.RLIMIT_SWAP)
print(soft, hard)
