# ping_statistics
My internet has been running shoddy lately (very bad ping). So I created this script to record my ping and a trace route and scheduled it to run every 30 minutes.

To make this work add ping_statistics.job.plist to ~/Library/LaunchAgents (if on a mac). If on Windows or Linux another scheduling method will be needed. You will need to edit the working directory to wherever you placed the ping_test.py. You will also have to create the folders "ping" and "traceroute" in that same directory. You will also have to run "chmod 755 ping_test.py" to change the permissions of the script to let launchd schedule it.

Note: Python 3 is required to run this script.
