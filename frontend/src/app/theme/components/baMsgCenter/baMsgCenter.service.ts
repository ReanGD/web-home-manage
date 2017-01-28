import {Injectable} from '@angular/core'

@Injectable()
export class BaMsgCenterService {

  private _notifications = [
    {
      image: 'assets/img/comments.svg',
      text: 'Vlad posted a new article.',
      time: '1 min ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Kostya changed his contact information.',
      time: '2 hrs ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'New orders received.',
      time: '5 hrs ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Andrey replied to your comment.',
      time: '1 day ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Today is Nasta\'s birthday.',
      time: '2 days ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'New comments on your post.',
      time: '3 days ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Kostya invited you to join the event.',
      time: '1 week ago'
    }
  ];

  private _messages = [
    {
      image: 'assets/img/comments.svg',
      text: 'After you get up and running, you can place Font Awesome icons just about...',
      time: '1 min ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'You asked, Font Awesome delivers with 40 shiny new icons in version 4.2.',
      time: '2 hrs ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Want to request new icons? Here\'s how. Need vectors or want to use on the...',
      time: '10 hrs ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Explore your passions and discover new ones by getting involved. Stretch your...',
      time: '1 day ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Get to know who we are - from the inside out. From our history and culture, to the...',
      time: '1 day ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Need some support to reach your goals? Apply for scholarships across a variety of...',
      time: '2 days ago'
    },
    {
      image: 'assets/img/comments.svg',
      text: 'Wrap the dropdown\'s trigger and the dropdown menu within .dropdown, or...',
      time: '1 week ago'
    }
  ];

  public getMessages():Array<Object> {
    return this._messages;
  }

  public getNotifications():Array<Object> {
    return this._notifications;
  }
}
