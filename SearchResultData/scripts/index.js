window.saveDataAcrossSessions = true;

//storing gaze points and time
var dataArray = [];
var aoiArray = [];

webgazer.showVideoPreview(false)
    .setGazeListener(function(data, elapsedTime) {
    if (data == null) {
        return;
    }
    var xprediction = data.x; //these x coordinates are relative to the viewport
    var yprediction = data.y; //these y coordinates are relative to the viewport
    
    console.log("Time: " + elapsedTime); //elapsed time is based on time since begin was called
    console.log("X prediction: " + xprediction);
    console.log("Y prediction: " + yprediction);

    // array for holding the current data points per row
    var rowArray = [];

    rowArray.push(elapsedTime);
    rowArray.push(xprediction);
    rowArray.push(yprediction);

    dataArray.push(rowArray);


}).begin();


function convertArrayOfObjectsToCsv(args) {
    var result, ctr, keys, columnDelimiter, lineDelimiter, data;

    data = args.data || null;
    if (data == null || !data.length) {
        return null;
    }

    columnDelimiter = args.columnDelimiter || ',';
    lineDelimiter = args.lineDelimiter || '\n';

    keys = Object.keys(data[0]);

    result = '';
    result += keys.join(columnDelimiter);
    result += lineDelimiter;

    data.forEach(function(item) {
        ctr = 0;
        keys.forEach(function(key) {
            if (ctr > 0) result += columnDelimiter;

            result += item[key];
            ctr++;
        });
        result += lineDelimiter;
    });

    return result;
}

function downloadCsv(args) {
    var data, filename, link;
    var csv = convertArrayOfObjectsToCsv({
        data: dataArray
    });

    if (csv == null) return;

    if(args !== null) {
        filename = 'testGazePoints.csv';
    }
    
    if (!csv.match(/^data:text\/csv/i)) {
        csv = 'data:text/csv;charset=utf-8,' + csv;
    }
    data = encodeURI(csv);

    link = document.createElement('a');
    link.setAttribute('href', data);
    link.setAttribute('download', filename);
    link.click();
}

