# algo
algo-backup


## quickfix broadcom driver issue

I've found a fix:

    Run the usual install

sudo apt install bcmwl-kernel-source

2. When it stops with the error, edit the file

sudo gedit /var/lib/dkms/bcmwl/6.30.223.271+bdcom/source/src/wl/sys/wl_linux.c

find PDE_DATA( and replace it with pde_data( . There should be 2 replaces total. Save the file.

3. Continue the installation with

sudo apt-get -f install

4. Enjoy =D
