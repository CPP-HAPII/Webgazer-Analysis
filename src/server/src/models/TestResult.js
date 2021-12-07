module.exports = function (sequelize, DataTypes) {
  return sequelize.define('testresult', {
    id: {
      type: DataTypes.INTEGER(11),
      allowNull: false,
      primaryKey: true,
      autoIncrement: true,
      field: 'ID'
    },
    userID: {
      type: DataTypes.INTEGER(11),
      allowNull: false,
      references: {
        model: 'Users',
        key: 'ID'
      },
      field: 'userID'
    },
    skill: {
      type: DataTypes.INTEGER(11),
      allowNull: false,
      field: 'SkillLevel'
    }
  }, {
    tableName: 'TestResult',
    timestamps: true
  })
}
