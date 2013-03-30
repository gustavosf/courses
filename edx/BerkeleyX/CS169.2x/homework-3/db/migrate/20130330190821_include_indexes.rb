class IncludeIndexes < ActiveRecord::Migration
  def up
    add_index :reviews, :movie_id
    add_index :reviews, :moviegoer_id
    add_index :movies, :id
    add_index :moviegoers, :id
  end

  def down
    remove_index :reviews, :movie_id
    remove_index :reviews, :moviegoer_id
    remove_index :movies, :id
    remove_index :moviegoers, :id
  end
end
