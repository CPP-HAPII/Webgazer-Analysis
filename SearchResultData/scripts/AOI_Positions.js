const LOOK_DELAY = 300; //make look or fixation duration 300 ms

let startLookTime = Number.POSITIVE_INFINITY;
let lookDirection = null;

var aoiArray = [];

// fixation counters per AOI
var r1Counter = 0;
var r2Counter = 0;
var r3Counter = 0;
var r4Counter = 0;
var r5Counter = 0;
var r6Counter = 0;
var notAOICounter = 0;

function getAOI() {
    // get AOI 1 positions
    var element1 = document.getElementById('c1');

    // **these values stay the same for all AOI's** 
    var leftPos = element1.getBoundingClientRect().left + window.scrollX;
    var rightPos = element1.getBoundingClientRect().right;
    console.log("Left Pos: " + leftPos + ", Right Pos: " + rightPos);


    var topPos1 = element1.getBoundingClientRect().top + window.scrollY;
    var bottomPos1 = element1.getBoundingClientRect().bottom;

    console.log("Top Pos 1: " + topPos1 + ", Bottom Pos 1: " + bottomPos1);

    // get AOI 2 positions
    var element2 = document.getElementById('c2');
    var topPos2 = element2.getBoundingClientRect().top + window.scrollY;
    var bottomPos2 = element2.getBoundingClientRect().bottom;
    console.log("Top Pos 2: " + topPos2 + ", Bottom Pos 2: " + bottomPos2);

    // get AOI 3 positions
    var element3 = document.getElementById('c3');
    var topPos3 = element3.getBoundingClientRect().top + window.scrollY;
    var bottomPos3 = element3.getBoundingClientRect().bottom;
    //console.log("x3: " + leftPos3 + ", y3: " + topPos3 + ", right3: " + rightPos3 + ", bottom3: " + bottomPos3);

    // get AOI 4 positions
    var element4 = document.getElementById('c4');
    var topPos4 = element4.getBoundingClientRect().top + window.scrollY;
    var bottomPos4 = element4.getBoundingClientRect().bottom;
    //console.log("x4: " + leftPos4 + ", y4: " + topPos4 + ", right4: " + rightPos4 + ", bottom4: " + bottomPos4);

    // get AOI 5 positions
    var element5 = document.getElementById('c5');
    var topPos5 = element5.getBoundingClientRect().top + window.scrollY;
    var bottomPos5 = element5.getBoundingClientRect().bottom;
    //console.log("x5: " + leftPos5 + ", y5: " + topPos5 + ", right5: " + rightPos5 + ", bottom5: " + bottomPos5);

    // get AOI 6 positions
    var element6 = document.getElementById('c6');
    var topPos6 = element6.getBoundingClientRect().top + window.scrollY;
    var bottomPos6 = element6.getBoundingClientRect().bottom;
    //console.log("x6: " + leftPos6 + ", y6: " + topPos6 + ", right6: " + rightPos6 + ", bottom6: " + bottomPos6);

    aoiArray = [
        [topPos1, bottomPos1],
        [topPos2, bottomPos2],
        [topPos3, bottomPos3],
        [topPos4, bottomPos4],
        [topPos5, bottomPos5],
        [topPos6, bottomPos6]
    ];

}

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

function downloadAoiCsv(args) {
    var data, filename, link;
    var csv = convertArrayOfObjectsToCsv({
        data: aoiArray
    });

    if (csv == null) return;

    if(args !== null) {
        filename = 'testAOI.csv';
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


