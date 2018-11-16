user='weblogic'
password='webl0gic'
url='t3://localhost:7101'

connect(user, password, url)

sca_deployComposite("http://localhost:7101", "sca_my-hello-world-soa-project_rev1.0.jar", user='weblogic', password='webl0gic', partition='default')
