module.exports = function (sequelize, DataTypes) {
    return sequelize.define('userAOIPositions', {
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
      leftPosition: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'LeftPosition'
      },
      rightPosition: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'RightPosition'
      },
      topAOIPos1: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'TopAOIPos1'
      },
      botAOIPos1: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'BotAOIPos1'
      },
      topAOIPos2: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'TopAOIPos2'
      },
      botAOIPos2: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'BotAOIPos2'
      },
      topAOIPos3: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'TopAOIPos3'
      },
      botAOIPos3: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'BotAOIPos3'
      },
      topAOIPos4: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'TopAOIPos4'
      },
      botAOIPos4: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'BotAOIPos4'
      },
      topAOIPos5: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'TopAOIPos5'
      },
      botAOIPos5: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'BotAOIPos5'
      },
      topAOIPos6: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'TopAOIPos6'
      },
      botAOIPos6: {
        type: DataTypes.DOUBLE,
        allowNull: false,
        field: 'BotAOIPos6'
      }
    }, {
      tableName: 'UserAOIPositions',
      timestamps: false
    })
  }