from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import os
import re

contact_bp = Blueprint('contact', __name__)

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_phone(phone):
    """Validate phone number format (optional)"""
    if not phone:
        return True  # Phone is optional
    pattern = r'^[\+]?[1-9]?\d{9,15}$'
    return re.match(pattern, phone.replace(' ', '').replace('-', '')) is not None

def save_contact_message(data):
    """Save contact message to file"""
    messages_file = 'data/messages.json'
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    # Load existing messages
    try:
        with open(messages_file, 'r') as f:
            messages = json.load(f)
    except FileNotFoundError:
        messages = []
    
    # Add new message
    message = {
        'id': len(messages) + 1,
        'name': data['name'],
        'email': data['email'],
        'phone': data.get('phone', ''),
        'subject': data.get('subject', 'Portfolio Contact'),
        'message': data['message'],
        'timestamp': datetime.now().isoformat(),
        'status': 'unread'
    }
    
    messages.append(message)
    
    # Save to file
    with open(messages_file, 'w') as f:
        json.dump(messages, f, indent=2)
    
    return message

@contact_bp.route('/contact', methods=['POST'])
def submit_contact_form():
    """Handle contact form submission"""
    try:
        # Get JSON data
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No data provided'}), 400
        
        # Validate required fields
        required_fields = ['name', 'email', 'message']
        for field in required_fields:
            if field not in data or not data[field].strip():
                return jsonify({'error': f'{field.capitalize()} is required'}), 400
        
        # Validate email format
        if not validate_email(data['email']):
            return jsonify({'error': 'Please provide a valid email address'}), 400
        
        # Validate phone if provided
        if 'phone' in data and data['phone'] and not validate_phone(data['phone']):
            return jsonify({'error': 'Please provide a valid phone number'}), 400
        
        # Check message length
        if len(data['message']) > 1000:
            return jsonify({'error': 'Message is too long (max 1000 characters)'}), 400
        
        # Save the message
        saved_message = save_contact_message(data)
        
        return jsonify({
            'success': True,
            'message': 'Thank you for your message! I will get back to you soon.',
            'id': saved_message['id']
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@contact_bp.route('/messages', methods=['GET'])
def get_messages():
    """Get all contact messages (admin endpoint)"""
    try:
        messages_file = 'data/messages.json'
        
        try:
            with open(messages_file, 'r') as f:
                messages = json.load(f)
        except FileNotFoundError:
            messages = []
        
        # Sort by timestamp (newest first)
        messages.sort(key=lambda x: x['timestamp'], reverse=True)
        
        return jsonify({
            'success': True,
            'messages': messages,
            'count': len(messages)
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500

@contact_bp.route('/messages/<int:message_id>', methods=['PUT'])
def update_message_status(message_id):
    """Update message status (mark as read/unread)"""
    try:
        data = request.get_json()
        status = data.get('status', 'read')
        
        messages_file = 'data/messages.json'
        
        try:
            with open(messages_file, 'r') as f:
                messages = json.load(f)
        except FileNotFoundError:
            return jsonify({'error': 'No messages found'}), 404
        
        # Find and update message
        message_found = False
        for message in messages:
            if message['id'] == message_id:
                message['status'] = status
                message_found = True
                break
        
        if not message_found:
            return jsonify({'error': 'Message not found'}), 404
        
        # Save updated messages
        with open(messages_file, 'w') as f:
            json.dump(messages, f, indent=2)
        
        return jsonify({
            'success': True,
            'message': f'Message status updated to {status}'
        }), 200
        
    except Exception as e:
        return jsonify({'error': f'Server error: {str(e)}'}), 500