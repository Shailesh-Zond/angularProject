import { Component } from '@angular/core';
import { UserService } from './user.service';
import { User } from './user.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  user: User = {
    username: '',
    email: '',
    contact: '',
    password: '',
    repassword: ''
  };
  isRegistering = false; // Toggle for showing registration form

  constructor(private userService: UserService) {}

  showRegisterForm() {
    this.isRegistering = true; // Show the register form
  }

  showLoginForm() {
    this.isRegistering = false; // Show the login form (if you have a login form)
  }

  onSubmit() {
    if (this.user.password !== this.user.repassword) {
      alert('Passwords do not match');
      return;
    }

    this.userService.registerUser(this.user).subscribe({
      next: (response) => {
        alert('Registration successful!');
      },
      error: (error) => {
        alert('Registration failed: ' + error.error.message);
      }
    });
  }
}
