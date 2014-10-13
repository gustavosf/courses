package course.labs.activitylab;

import android.app.Activity;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.Button;
import android.widget.TextView;

public class ActivityOne extends Activity {

	// Use these as keys when you're saving state between reconfigurations
	private static final String RESTART_KEY = "restart";
	private static final String RESUME_KEY = "resume";
	private static final String START_KEY = "start";
	private static final String CREATE_KEY = "create";

	// String for LogCat documentation
	private final static String TAG = "Lab-ActivityOne";

	// Lifecycle counters

	// TODO: DONE
	// Create variables named
	// mCreate, mRestart, mStart and mResume
	// to count calls to onCreate(), onRestart(), onStart() and
	// onResume(). These variables should not be defined as static.
    private int mCreate = 0;
    private int mRestart = 0;
    private int mStart = 0;
    private int mResume = 0;

	// You will need to increment these variables' values when their
	// corresponding lifecycle methods get called.

	// TODO: DONE
	// Create variables for each of the TextViews
    private TextView mTvCreate;
    private TextView mTvRestart;
    private TextView mTvStart;
    private TextView mTvResume;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_one);

		// TODO: DONE
		// Assign the appropriate TextViews to the TextView variables
        mTvCreate = (TextView) findViewById(R.id.create);
        mTvRestart = (TextView) findViewById(R.id.restart);
        mTvStart = (TextView) findViewById(R.id.start);
        mTvResume = (TextView) findViewById(R.id.resume);

		Button launchActivityTwoButton = (Button) findViewById(R.id.bLaunchActivityTwo);
		launchActivityTwoButton.setOnClickListener(new OnClickListener() {

			@Override
			public void onClick(View v) {
				// TODO: DONE
				// Launch Activity Two
				// Hint: use Context's startActivity() method

                // Create an intent stating which Activity you would like to
				// start
				Intent intent = new Intent(ActivityOne.this, ActivityTwo.class);

				// Launch the Activity using the intent
                startActivity(intent);

			}
		});

		// Has previous state been saved?
		if (savedInstanceState != null) {

			// TODO: DONE
			// Restore value of counters from saved state
			// Only need 4 lines of code, one for every count variable
            savedInstanceState.getInt("mStart", mStart);
            savedInstanceState.getInt("mRestart", mRestart);
            savedInstanceState.getInt("mResume", mResume);
            savedInstanceState.getInt("mCreate", mCreate);

		}

		// Emit LogCat message
		Log.i(TAG, "Entered the onCreate() method");

		// TODO: DONE
		// Update the appropriate count variable
		// Update the user interface via the displayCounts() method
        mCreate += 1;
        displayCounts();

	}

	// Lifecycle callback overrides

	@Override
	public void onStart() {
		super.onStart();

		// Emit LogCat message
		Log.i(TAG, "Entered the onStart() method");

		// TODO: DONE
		// Update the appropriate count variable
		// Update the user interface
        mStart += 1;
        displayCounts();

	}

	@Override
	public void onResume() {
		super.onResume();

		// Emit LogCat message
		Log.i(TAG, "Entered the onResume() method");

		// TODO: DONE
		// Update the appropriate count variable
		// Update the user interface
        mResume += 1;
        displayCounts();

	}

	@Override
	public void onPause() {
		super.onPause();

		// Emit LogCat message
		Log.i(TAG, "Entered the onPause() method");
	}

	@Override
	public void onStop() {
		super.onStop();

		// Emit LogCat message
		Log.i(TAG, "Entered the onStop() method");
	}

	@Override
	public void onRestart() {
		super.onRestart();

		// Emit LogCat message
		Log.i(TAG, "Entered the onRestart() method");

		// TODO: DONE
		// Update the appropriate count variable
		// Update the user interface
        mRestart += 1;
        displayCounts();

	}

	@Override
	public void onDestroy() {
		super.onDestroy();

		// Emit LogCat message
		Log.i(TAG, "Entered the onDestroy() method");
	}

	@Override
	public void onSaveInstanceState(Bundle savedInstanceState) {
		// TODO: DONE
		// Save state information with a collection of key-value pairs
		// 4 lines of code, one for every count variable
        savedInstanceState.putInt("mStart", mStart);
        savedInstanceState.putInt("mRestart", mRestart);
        savedInstanceState.putInt("mResume", mResume);
        savedInstanceState.putInt("mCreate", mCreate);

	}

	// Updates the displayed counters
	// This method expects that the counters and TextView variables use the
	// names
	// specified above
	public void displayCounts() {
        mTvCreate.setText("onCreate() calls: " + mCreate);
		mTvStart.setText("onStart() calls: " + mStart);
		mTvResume.setText("onResume() calls: " + mResume);
		mTvRestart.setText("onRestart() calls: " + mRestart);

	}
}
