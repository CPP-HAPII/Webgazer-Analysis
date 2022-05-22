module.exports = {
  port: process.env.PORT || 8081,
  db: {
    database: process.env.DB_NAME || 'HAPII',
    user: process.env.DB_USER || 'root',
    password: process.env.DB_PASS || 'CPPHapii',
    options: {
      dialect: process.env.DIALECT || 'mysql',
      host: process.env.HOST || 'aa1bk9bp1u7gv96.c2geutczdb6x.us-west-1.rds.amazonaws.com', // 'aa13mnjbzyz2hfy.ciyfv2p6bkbk.us-west-1.rds.amazonaws.com' 'hapiidb.c5hxam6fwt9f.us-west-1.rds.amazonaws.com',
      port: 3306,
      omitNull: true,
      timezone: 'AMERICA/LOS_ANGELES'
    }
  }
}
