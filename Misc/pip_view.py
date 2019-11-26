
import pip

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s, ver.%s" % (i.key, i.version) for i in installed_packages])
fout=open("pip_list.txt", "w")
for line in installed_packages_list:
    fout.write(line+'\n')
