# lobster

### A two server song downloading system using TCP connection.

</br>

## **Definition:**
Consists of two servers and multiple clients. Clients can request the song list, request to check for a song and request to download a song. The song list is shared and at least one of the servers must contain the song on the list and could be downloaded. If both servers have the song, the song will be downloaded from clients preferred one.

</br>

Python and its libraries _socket_, _threading_, _os_ and _json_ are used. Server and client files are written separately, song list and user list created as both json files. _The Age of the Understatement_ album from _The Last Shadow Puppets_ used for creating a song list.

</br>

## **Usage:**


1. Cloning repository:

    `$ git clone https://github.com/tugberkozkara/lobster.git`

2. Getting into the project:

    `$ cd lobster/`


Servers can be run by calling server.py file with identifying the server number.

```
    $ cd server/
    $ python server.py
    Server number 1 or 2>>> 1
    Server1 is running...
```
```
    $ cd server/
    $ python server.py
    Server number 1 or 2>>> 2
    Server2 is running...
```

While both servers are running, clients can be run.

```
    $ cd client/
    $ python client.py
    Enter username: client1
    Enter password: client1

    Logged in successfully.
```

Once client typed correct username-password correlation defined in server/users.json file, the system becomes reachable. It can be seen on servers.

```
Connected with 127.0.0.1:57499
User 'client1' logged in successfully.
```

Clients can send 4 different requests to servers;
```
get         Gets the list of songs from the server.
check       Check if a song exists in database.
download    Download a song from song list.
exit        Exit the program.

Enter the command:
```

</br>
</br>

## Example Requests:

* get

```
Enter the command: get

['The Age Of The Understatement','Standing Next To Me', 'Calm Like You',
'Separate And Ever Deadly', 'The Chamber', 'Only The Truth',
'My Mistakes Were Made For You', 'Black Plant', "I Don't Like You Anymore",
'In My Room', 'Meeting Place', 'The Time Has Come Again']
```

* check

```
Enter the command: check Standing Next To Me

Song 'Standing Next To Me' found in server1.
```

* download

If the song exists only one server, it will be downloaded directly.

```
Enter the command: download Standing Next To Me
Downloaded!
```

But if the song exists on both servers, clients are free to choose the server.
```
Enter the command: download Calm Like You
Choose your preferred server 1 or 2: 2
Downloaded!
```

* exit

```
Enter the command: exit
```
```
User 'client1' logged out.
```
