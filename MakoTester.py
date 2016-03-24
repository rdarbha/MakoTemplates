from mako.template import Template

name_of_file='MakoTemplate' 

mytemplate = Template(filename=name_of_file)
print(mytemplate.render())
