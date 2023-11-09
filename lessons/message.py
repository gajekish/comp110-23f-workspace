"""Class to store a message (operator overload, union types, default parameters)."""

class Message:

    to: str | int
    content: str 
    important: bool

    def __init__(self, recipient: str | int, message_content: str = "", importance_flag: bool = False) -> None:
        """Construct a message."""
        self.to = recipient
        self.content = message_content
        self.important = importance_flag

    def __str__(self) -> str:
        """String operator overload"""
        output: str = f"Message to {self.to}:\n"
        output += f"Important? {self.important}\n"
        output += f"{self.content}"
        return output
    
    def __mul__(self, factor: int):
        """Multiplication operator overload."""
        copy_val: str = self.content
        for loop_number in range(1, factor):
            self.content += " " + copy_val


msg_to_prasun: Message = Message("Prasun", "Do your 110 homework and stop sleeping!", True)
print(msg_to_prasun)
print("\n")
msg_to_myself: Message = Message(730662291, "Always stay productive, do not waste time!")
print(msg_to_myself)
print("\n")
msg_to_someone: Message = Message("someone")
msg_to_someone.to = "Person"
msg_to_someone.content = "Hello!"
print(msg_to_someone)