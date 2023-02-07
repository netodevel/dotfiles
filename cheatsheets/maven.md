### run specific groups
`mvn -Dgroups="integration, fast, feature-168"`

### Exclude tests which tagged with 'slow'
$ mvn -DexcludedGroups="slow"

### Build a specific module in multi module project
mvn --projects $module-name --also-make install -DskipTests