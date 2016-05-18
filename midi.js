var exec = require('child_process').exec;
var cmd = './midi.py';

module.exports = function(RED) {
    function Midi(config) {
        RED.nodes.createNode(this, config);
        var node = this;
        this.on('input', function(msg) {
            // msg.payload
            exec(cmd, function(error, stdout, stderr) {
              // command output is in stdout
            });
        });
    }
    RED.nodes.registerType("midi", Midi);
}
