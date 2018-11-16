user='weblogic'
password='webl0gic'
url='t3://localhost:7101'

connect(user, password, url)

sca_deployComposite("http://localhost:7101", "sca_CELFServiceWrapper.jar", user='weblogic', password='webl0gic', partition='default')