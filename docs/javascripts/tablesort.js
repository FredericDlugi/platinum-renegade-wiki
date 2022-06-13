    (function () {
        var cleanNumber = function (i) {
            if (i == "-") {
                return 0
            }
            return i.replace(/[^\-?0-9.]/g, '');
        },

            compareNumber = function (a, b) {
                a = parseFloat(a);
                b = parseFloat(b);

                a = isNaN(a) ? 0 : a;
                b = isNaN(b) ? 0 : b;

                return a - b;
            };

        Tablesort.extend('move_number', function (item) {
            return item.match(/^[-+]?[£\x24Û¢´€]?\d+\s*([,\.]\d{0,2})/) || // Prefixed currency
                item.match(/^[-+]?\d+\s*([,\.]\d{0,2})?[£\x24Û¢´€]/) || // Suffixed currency
                item.match(/^[-+]?(\d)*-?([,\.]){0,1}-?(\d)+([E,e][\-+][\d]+)?%?$/) || // Number
                item == "-"; // One dash
        }, function (a, b) {
            a = cleanNumber(a);
            b = cleanNumber(b);

            return compareNumber(b, a);
        });
    }());


    document$.subscribe(function () {
        var tables = document.querySelectorAll("article table:not([class])")
        tables.forEach(function (table) {
            new Tablesort(table)
        })
    })
