css = '''
<style>
  body {
    background-color: #1a1a1a;
    color: #ffffff;
    font-family: 'Arial', sans-serif;
  }

  .chat-message {
    padding: 1rem;
    border-radius: 0.5rem;
    margin-bottom: 1rem;
    display: flex;
    align-items: flex-start;
  }

  .chat-message.user {
    background-color: #333333;
  }

  .chat-message.bot {
    background-color: #555555;
  }

  .chat-message .avatar {
    width: 10%;
    margin-right: 1rem;
  }

  .chat-message .avatar img {
    max-width: 100%;
    max-height: 100%;
    border-radius: 50%;
    object-fit: cover;
  }

  .chat-message .message {
    width: 90%;
    padding: 0.5rem;
    background-color: #444444;
    border-radius: 0.25rem;
    box-shadow: 0 0.125rem 0.25rem rgba(0, 0, 0, 0.5);
    color: #ffffff;
  }
</style>
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img src="https://i.ibb.co/GxFxZjj/image1.png">
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
user_template = '''
<div class="chat-message user">
    <div class="message">{{MSG}}</div>
    <div class="avatar">
        <img src="https://i.ibb.co/GxFxZjj/image1.png">
    </div>  
'''