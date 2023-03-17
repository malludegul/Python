class RecentlyPlayedStore:
    def __init__(self, initial_capacity, max_songs_per_user):
        self.max_songs_per_user = max_songs_per_user
        self.users = {}
        self.capacity = initial_capacity
        self.played_songs = ()
    
    def add_song_for_user(self, user_id, song_id):
        # Check if the user already exists in the store
        if user_id in self.users:
            # Get the user's playlist
            playlist = self.users[user_id]
            
            # Check if the song is already in the playlist
            if song_id in playlist:
                # If the song is already in the playlist, move it to the front of the list
                node = playlist[song_id]
                self.played_songs.move_to_front(node)
            else:
                # If the song is not in the playlist, add it to the front of the list
                node = self.played_songs.add_to_front(song_id)
                playlist[song_id] = node
                
                # Check if the user's playlist has reached the maximum number of songs
                if len(playlist) > self.max_songs_per_user:
                    # If the playlist is full, remove the least recently played song
                    least_recently_played_node = self.played_songs.tail
                    least_recently_played_song = least_recently_played_node.data
                    
                    # Remove the song from the playlist and the doubly linked list
                    del playlist[least_recently_played_song]
                    self.played_songs.remove_node(least_recently_played_node)
        else:
            # If the user does not exist in the store, create a new playlist and add the song to it
            playlist = {}
            node = self.played_songs.add_to_front(song_id)
            playlist[song_id] = node
            self.users[user_id] = playlist





