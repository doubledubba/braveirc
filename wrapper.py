from server import main
import os

child_pid = os.fork()
if child_pid == 0:
    main()
