class MoviesController < ApplicationController

  def show
    id = params[:id] # retrieve movie ID from URI route
    @movie = Movie.find(id) # look up movie by unique ID
    # will render app/views/movies/show.<extension> by default
  end

  def index
    @sort = params[:sort] || session[:sort] || :id
    @all_ratings = Movie.all_ratings
    @selected_ratings = params[:ratings] || session[:ratings] || Hash[@all_ratings.map{|x|[x,1]}]
    @movies = Movie.find_all_by_rating @selected_ratings.keys, :order => @sort

    if params[:sort] != @sort or params[:ratings] != @selected_ratings
      session[:sort] = @sort
      session[:ratings] = @selected_ratings
      redirect_to :sort => @sort, :ratings => @selected_ratings
    end
  end

  def new
    # default: render 'new' template
  end

  def create
    @movie = Movie.create!(params[:movie])
    flash[:notice] = "#{@movie.title} was successfully created."
    redirect_to movies_path
  end

  def edit
    @movie = Movie.find params[:id]
  end

  def update
    @movie = Movie.find params[:id]
    @movie.update_attributes!(params[:movie])
    flash[:notice] = "#{@movie.title} was successfully updated."
    redirect_to movie_path(@movie)
  end

  def destroy
    @movie = Movie.find(params[:id])
    @movie.destroy
    flash[:notice] = "Movie '#{@movie.title}' deleted."
    redirect_to movies_path
  end

end
