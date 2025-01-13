from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

# Define the command for searching
@Client.on_message(filters.command("search") & filters.private)
async def search_movie(client: Client, message: Message):
    # Check if the user provided a movie name
    if len(message.command) < 2:
        await message.reply_text("Please provide the name of the movie after /search.")
        return

    # Extract the movie name from the command
    movie_name = " ".join(message.command[1:])

    # Step 1: Send a "searching" message
    searching_message = await message.reply_text(f"Searching for '{movie_name}', please wait...")

    # Step 2: Simulate the search process (replace this with your actual logic)
    await asyncio.sleep(5)  # Replace with actual search logic (e.g., database or API call)

    # Step 3: Send the search results
    # Replace this with your actual search result
    movie_details = f"Details about the movie '{movie_name}':\n[Sample movie details here]."

    await searching_message.edit_text(movie_details)
