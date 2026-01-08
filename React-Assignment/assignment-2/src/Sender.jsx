function Sender({ onMessageChange }) {
    return (
        <div>
            <h3>Sender</h3>
            <input
                type="text"
                placeholder="Type a message..."
                onChange={(e) => onMessageChange(e.target.value)}
            />
        </div>
    );
}

export default Sender;
