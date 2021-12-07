module.exports = function (sequelize, DataTypes) {
    return sequelize.define('userGaze', {
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
      qID: {
        type: DataTypes.INTEGER(11),
        allowNull: false,
        primaryKey: true,
        references: {
          model: 'SearchQuery',
          key: 'ID'
        },
        field: 'qID'
      }, 
      gazePoints: {
        type: DataTypes.TEXT('long'),
        allowNull: false,
        field: 'GazePoints'
      }
    }, {
      tableName: 'UserGaze',
      timestamps: true
    })
  }
  