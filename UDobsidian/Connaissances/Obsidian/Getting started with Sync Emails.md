# Getting started with Sync Emails
#mail #courriels 

Plugins Mail:
Welcome and thank you for installing Sync Emails by TaskRobin for Obsidian! This plugin helps you maintain a searchable archive of important emails directly within your Obsidian vault.

## How TaskRobin Works

TaskRobin creates a seamless bridge between your email inbox and Obsidian:

1. **Email Forwarding**: You forward selected emails from your email inbox to a TaskRobin forwarding email address that you choose
2. **Automatic Processing**: TaskRobin securely processes these emails and their attachments, the emails are converted to markdown files
3. **Obsidian Integration**: Hit the "Sync now" button to download your forwarded emails into your Obsidian vault

## Setup Guide

### 1. Configure the Plugin

- Click the TaskRobin icon in the Obsidian ribbon (envelope icon)
- Enter your email address (the one you'll forward emails from)
- Create a unique forwarding address (e.g., `yourname@taskrobin.io`)
- Choose where emails should be saved in your vault

### 2. Send Emails to the Forwarding Address

To save emails to your Obsidian, send emails from your registered email address to the TaskRobin forwarding address from step 1.

You can simply send, forward, CC or BCC emails one by one to your TaskRobin forward address, or setup auto forwarding with your email provider - [[#Set Up Email Auto Forwarding]]

### 3. Sync Your Emails

- Click the TaskRobin icon in the Obsidian ribbon
- Select "Sync now" to download your emails
- Emails will be saved as markdown files in your designated folder

## File Organization

Emails are saved with the following structure:

```
Your-Vault/
└── Emails/ # Default directory (configurable)
	├── YYYY-MM-DD-{email subject line}/ # Date-based folders
	│   ├── email.md # Email content
	│   ├── attachment1.pdf # Email attachments
	│   └── attachment2.html # Email attachments
	└── ...
```

## Subscription Information

- TaskRobin offers a 7-day free trial for all new users
- No payment information required during the trial to access all features
- Subscription plans start at $2.49/month after the trial period
- Visit [TaskRobin.io](https://www.taskrobin.io) for pricing details

## Need Help?

- Visit [TaskRobin.io](https://www.taskrobin.io) for more information
- Contact us through [Live chat support](https://app.taskrobin.io)

Thank you for choosing TaskRobin! We hope this plugin enhances your Obsidian workflow.

## Set Up Email Auto Forwarding

Depending on your email provider, set up forwarding for emails you want to save:

**Gmail**:
- Open Gmail Settings > Forwarding and POP/IMAP
- Click "Add a forwarding address" and enter your TaskRobin address
- Choose to forward selected emails or set up a filter

**Outlook**:
- Go to Settings > Mail > Forwarding
- Enter your TaskRobin forwarding address
- Choose whether to keep copies of forwarded messages

**Apple Mail**:
- Go to Mail > Preferences > Rules
- Create a new rule to forward specific emails to your TaskRobin address

