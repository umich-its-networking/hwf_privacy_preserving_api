(function() {
    // Create the connector object
    var myConnector = tableau.makeConnector();

    // Define the schema
    myConnector.getSchema = function(schemaCallback) {
        var cols = [{
            id: "count",
            dataType: tableau.dataTypeEnum.string
        }
	];

        var tableSchema = {
            id: "PrivacyPreservingApi",
            alias: "Privacy preserving api data",
            columns: cols
        };

        schemaCallback([tableSchema]);
    };

    // Download the data
    myConnector.getData = function(table, doneCallback) {
        $.getJSON("http://localhost:8889/hwf-privacy-api.dsc.umich.edu/student/count/?query=age==16", function(resp) {
           // var feat = resp.features;
                tableData = [];

                tableData.push({
                    "count": resp.count
                });

            table.appendRows(tableData);
            doneCallback();
        });
    };

    tableau.registerConnector(myConnector);

    // Create event listeners for when the user submits the form
    $(document).ready(function() {
        $("#submitButton").click(function() {
            tableau.connectionName = "Privacy Preserving API"; // This will be the data source name in Tableau
            tableau.submit(); // This sends the connector object to Tableau
        });
    });
})();
